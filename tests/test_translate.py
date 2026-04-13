import sys
from pathlib import Path
import tempfile
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from translate import read_input


def test_read_txt():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False, encoding="utf-8") as f:
        f.write("يَا ابْنَ الإِنسَانِ\n\nكُنْتُ فِي قِدَمِ الذَّاتِ")
        f.flush()
        result = read_input(Path(f.name))
    assert "يَا ابْنَ الإِنسَانِ" in result
    assert "كُنْتُ فِي قِدَمِ الذَّاتِ" in result


def test_read_docx():
    import docx
    with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as f:
        doc = docx.Document()
        doc.add_paragraph("يَا ابْنَ الإِنسَانِ")
        doc.add_paragraph("كُنْتُ فِي قِدَمِ الذَّاتِ")
        doc.save(f.name)
        result = read_input(Path(f.name))
    assert "يَا ابْنَ الإِنسَانِ" in result
    assert "كُنْتُ فِي قِدَمِ الذَّاتِ" in result


def test_read_unsupported_type():
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
        f.write(b"fake pdf")
        f.flush()
        with pytest.raises(SystemExit):
            read_input(Path(f.name))


from translate import count_paragraphs, fix_paragraph_count


def test_count_paragraphs():
    assert count_paragraphs("one\n\ntwo\n\nthree") == 3
    assert count_paragraphs("single block") == 1
    assert count_paragraphs("") == 0
    assert count_paragraphs("a\n\n\n\nb") == 2  # extra blank lines still 2 paras


def test_fix_paragraph_count_too_many():
    text = "Short.\n\nAlso short.\n\nThis is the longest paragraph here.\n\nTiny."
    fixed = fix_paragraph_count(text, target=3)
    assert count_paragraphs(fixed) == 3
    # Merges the two shortest adjacent paragraphs
    assert "Short. Also short." in fixed


def test_fix_paragraph_count_too_few():
    text = "First sentence. Second sentence. Third sentence. Fourth sentence."
    fixed = fix_paragraph_count(text, target=2)
    assert count_paragraphs(fixed) == 2


def test_fix_paragraph_count_already_correct():
    text = "one\n\ntwo\n\nthree"
    fixed = fix_paragraph_count(text, target=3)
    assert fixed == text


import subprocess

@pytest.mark.integration
def test_end_to_end_cli():
    """Smoke test: translate a short Arabic text via the CLI."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False, encoding="utf-8") as f:
        # First Arabic Hidden Word
        f.write("يَا ابْنَ الإِنسَانِ كُنْتُ فِي قِدَمِ الذَّاتِ وَأَزَلِيَّةِ الكَيْنُونَةِ "
                "فِي مَهْدِ كَيْنُونَتِيَ عَرَفْتُ حُبِّي فِيكَ فَخَلَقْتُكَ وَأَلْقَيْتُ "
                "عَلَيْكَ مِثَالِي وَأَظْهَرْتُ لَكَ جَمَالِي")
        f.flush()
        input_path = f.name

    output_path = input_path + ".out.txt"
    result = subprocess.run(
        ["uv", "run", "python", "translate.py", input_path, "-o", output_path],
        cwd=str(Path(__file__).resolve().parent.parent),
        capture_output=True, text=True, timeout=120,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    output = Path(output_path).read_text(encoding="utf-8")
    # Should contain archaic English (thee/thou)
    assert any(word in output.lower() for word in ["thee", "thou", "thy", "thine"])
    # Should not contain "you" or "your"
    words = output.lower().split()
    assert "you" not in words
    assert "your" not in words
    # Cleanup
    Path(input_path).unlink(missing_ok=True)
    Path(output_path).unlink(missing_ok=True)

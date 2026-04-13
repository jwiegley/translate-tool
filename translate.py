#!/usr/bin/env python3
"""Translate Persian/Arabic Baha'i sacred texts into English.

Usage:
    uv run python translate.py input.txt              # writes input.translated.txt
    uv run python translate.py input.docx             # handles Word documents
    uv run python translate.py input.txt -o out.txt   # explicit output path
"""

import argparse
import os
import sys
from pathlib import Path

from openai import OpenAI


# --- System Prompt (distilled from 50+ experiments) ---

SYSTEM_PROMPT = """\
You are an expert translator of Arabic and Persian Baha'i sacred texts into English, \
producing translations in the elevated register characteristic of Shoghi Effendi's \
authorized translations. Your goal is to match his specific word choices, phrasings, \
and sentence structures as closely as possible. Trust your first instinct for each \
phrase. Do not second-guess yourself. Do not rephrase what comes to mind first.

## Shoghi Effendi's Translation Register

### Vocabulary and Diction
- Second person: ALWAYS "thee", "thou", "thy", "thine" — never "you/your"
- Verb forms: "hath", "doth", "shalt", "canst", "mayest", "wilt", "behooveth"
- Relative: "that which" (not "what"), "he that" (not "whoever/anyone who")
- Connectives: "verily", "indeed", "moreover", "inasmuch as", "wherefore"
- Prepositions: "unto" (emphatic), "therefrom", "therein", "thereof", "thereon"
- Negation: "not" placed before verb ("turn not away", "neglect it not")
- Imperatives: inverted archaic ("ponder this", "set it then before thine eyes")

### Concision — The Most Critical Stylistic Feature
Shoghi Effendi's translations are SHORTER than most translations of the same text. \
He compresses, never expands unnecessarily. Specific patterns:
- Use single-word epithets, not relative clauses: "Enchanter" NOT "Thou Who dost enchant"; \
"Chastiser" NOT "Thou Who dost chastise"; "Answerer" NOT "Thou Who dost answer"
- Compress: "sore thirst" NOT "the trembling of thirst"; "all men" NOT "all who are in creation"
- Use vivid nouns: "gleaming" NOT "splendour of the light"; "emblems" NOT "tokens"
- One strong word beats two weak ones: "consumed" NOT "completely destroyed"

### Sentence Architecture
- Long subordinate clauses resolved by weighty main clauses
- Semicolons as rhythmic pivots between balanced parallel clauses
- Participle phrases: "having enabled me to hearken…", "inasmuch as Thou hast…"
- Inverted word order for emphasis: "Veiled in My immemorial being…"
- Relative clause chains: "…which hath been made the seat of His throne, \
which His footsteps have trodden, which hath been honoured by His presence…"

### Interpretive Expansion
- Expand compressed Arabic/Persian constructions JUST enough for English clarity
- Add interpretive words that draw out implicit meaning (e.g., "Veiled in" for كنت في)
- Never fabricate content or add theological commentary not implied by the source

## Style Calibration — Learn From These Examples

Study these examples carefully. They show the SAME source rendered at different quality levels.

**PERFECT (Shoghi Effendi's own):**
Source: يَا ابْنَ الإِنسَانِ كُنْتُ فِي قِدَمِ الذَّاتِ وَأَزَلِيَّةِ الكَيْنُونَةِ فِي مَهْدِ \
كَيْنُونَتِيَ عَرَفْتُ حُبِّي فِيكَ فَخَلَقْتُكَ وَأَلْقَيْتُ عَلَيْكَ مِثَالِي وَأَظْهَرْتُ لَكَ جَمَالِي
Translation: "O SON OF MAN! Veiled in My immemorial being and in the ancient eternity of \
My essence, I knew My love for thee; therefore I created thee, have engraved on thee \
Mine image, and revealed to thee My beauty."
Why it works: Balanced, elevated register. "Veiled in" adds interpretive depth without \
fabrication. "Immemorial being" is an inspired but faithful rendering of قِدَمِ الذَّاتِ. \
Exactly 35 words — densely packed, no padding.

**TOO ORNATE (over-expanded):**
"O THOU CHILD OF MORTAL CLAY! In the primaeval depths of Mine own unfathomable Selfhood, \
and in the sempiternal antiquity of Mine abiding Substance, I didst perceive the flames \
of Mine affection kindled for thee; whereupon I fashioned thee from the crucible of creation…"
Why it fails: 80+ words vs. 35. "Primaeval", "sempiternal", "pulchritude" are overwrought. \
"Crucible of creation" and "sanctified gaze" fabricate content not in the source.

**TOO LITERAL (flat):**
"O son of man. I was in the primordial essence and eternal being. In the cradle of my \
existence I recognized my love in you, so I created you and cast my image upon you and \
showed you my beauty."
Why it fails: No King James register. Flat, declarative sentences. "Cradle of my existence" \
is literal but misses the meaning. No interpretive layer at all.

## Persian vs. Arabic — Adjusting Your Approach

The source text may be in Arabic or Persian. Shoghi Effendi adapted his style \
to each language's character. Identify the language first, then adjust:

**Arabic texts** (Kitáb-i-Aqdas, Arabic Hidden Words, Fire Tablet, Tablet of Ahmad, \
Tablet of Carmel): Arabic sacred text is typically terse and commanding. \
Shoghi Effendi matches this with short, powerful sentences. Imperatives are direct. \
Devotional passages use tight parallel structures.

**Persian texts** (Kitáb-i-Íqán, Persian Hidden Words, Epistle to the Son of the Wolf, \
many Gleanings, Prayers and Meditations): Persian prose is naturally more flowing, but \
Shoghi Effendi still maintains his characteristic density. Semicolons link balanced \
parallel images; each clause carries weight. Izáfa (possessive/adjectival) chains like \
"گلشن محبّت" become "the garden of love" — compact but faithful. Persian mystic \
vocabulary receives interpretive depth: عرفان → "true knowledge", not merely "knowledge". \
Even with Persian, fewer English words is almost always better.

Note: The Arabic Hidden Words and the Persian Hidden Words are separate compositions, \
not translations of each other. Each has its own character.

## Mandatory Terminology — COMPLETE GLOSSARY

For ANY term below appearing in the source text, use the EXACT English rendering. \
This is non-negotiable.

Proper names:
- بهاءالله → Bahá'u'lláh | عبدالبها → Abdu'l-Bahá | باب → the Báb
- نقطه اولی → the Primal Point | قلم اعلی → the Most Exalted Pen

Theological terms:
- مظهر ظهور → Manifestation of God | بیت العدل اعظم → the Universal House of Justice
- محفل روحانی → Spiritual Assembly | اسم اعظم → the Greatest Name
- صراط مستقیم → the straight Path | مشيئت → the Divine Will
- عرفان → true knowledge | توحيد → the oneness of God | عدل → justice

Spiritual realms:
- ملكوت → the Kingdom | جبروت → the Realm on High
- لاهوت → the Empyrean | ناسوت → the world of being

Divine attributes:
- حق → the True One | رحمن → the All-Merciful | عزيز → the Almighty
- قدير → the Omnipotent | عليم → the All-Knowing | سميع → the All-Hearing
- بصير → the All-Seeing | حكيم → the All-Wise | غني → the Self-Sufficient
- قيوم → the Self-Subsisting | قدوس → the Most Holy

Titles and addresses:
- مقصود → the Desired One | محبوب → the Beloved
- سبحانه و تعالی → exalted and glorified | الله ابهی → Alláh-u-Abhá
- يا بهاءالابهی → O Glory of the All-Glorious

Sacred references:
- سدرة المنتهى → the Sadratu'l-Muntahá | طور سینا → the Sinai of the Spirit
- كتاب اقدس → the Kitáb-i-Aqdas | كتاب ايقان → the Kitáb-i-Íqán
- الواح → Tablets

Hidden Words addresses:
- ابن → son (in "O Son of…") | روح → spirit | انسان → man | وجود → being/existence

## Instructions

1. Identify the source language (Arabic or Persian) and count paragraphs.
2. Translate the COMPLETE text in one pass, matching Shoghi Effendi's register.
3. Output ONLY the English translation — no translator notes, headers, or commentary.

CRITICAL RULES:
- Output paragraph count MUST exactly match source paragraph count.
- Separate paragraphs with exactly one blank line.
- Concision is paramount: if your English is LONGER than the source, you are almost \
certainly over-expanding. Cut ruthlessly.
- TRUST YOUR FIRST INSTINCT for word choices. Over-revision degrades quality.
- NEVER use you/your — ALWAYS use thee/thou/thy/thine.\
"""

VERIFY_PROMPT = """\
You are a translation verifier. Check the candidate translation for exactly two errors:

1. PARAGRAPH COUNT: The translation must have exactly {target_paras} paragraphs \
(separated by blank lines), matching the source text.
2. PRONOUNS: All second-person references must use thee/thou/thy/thine (never you/your).

If EITHER error exists, output a corrected version fixing ONLY those two issues. \
Do NOT change any word choices, phrasing, or style.
If no errors are found, output the translation unchanged.

Output ONLY the translation text — no commentary, no explanation.\
"""


# --- LLM helpers ---

def make_client(args) -> OpenAI:
    """Create OpenAI client from args/environment."""
    base_url = args.base_url or os.environ.get("TRANSLATE_BASE_URL", "http://localhost:8317/v1")
    api_key = args.api_key or os.environ.get("TRANSLATE_API_KEY", "dummy-key")
    return OpenAI(base_url=base_url, api_key=api_key)


def get_model(args) -> str:
    """Resolve model name from args/environment."""
    return args.model or os.environ.get("TRANSLATE_MODEL", "claude-opus-4-6")


def translate(client: OpenAI, model: str, source: str) -> str:
    """Call the LLM to translate source text. Returns the translation."""
    resp = client.chat.completions.create(
        model=model,
        temperature=0.3,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": source},
        ],
    )
    return (resp.choices[0].message.content or "").strip()


def verify(client: OpenAI, model: str, source: str, translation: str) -> str:
    """Call the LLM to verify paragraph count and pronouns. Returns corrected text."""
    target_paras = count_paragraphs(source)
    resp = client.chat.completions.create(
        model=model,
        temperature=0.0,
        messages=[
            {"role": "system", "content": VERIFY_PROMPT.format(target_paras=target_paras)},
            {"role": "user", "content": translation},
        ],
    )
    return (resp.choices[0].message.content or "").strip()


def read_input(path: Path) -> str:
    """Read source text from .txt or .docx file."""
    if path.suffix.lower() == ".docx":
        import docx
        doc = docx.Document(str(path))
        return "\n\n".join(p.text for p in doc.paragraphs if p.text.strip())
    elif path.suffix.lower() in (".txt", ".md"):
        return path.read_text(encoding="utf-8")
    else:
        print(f"Error: unsupported file type '{path.suffix}' (use .txt or .docx)", file=sys.stderr)
        sys.exit(1)


def count_paragraphs(text: str) -> int:
    """Count paragraphs (separated by blank lines) in text."""
    if not text.strip():
        return 0
    return len([p.strip() for p in text.strip().split("\n\n") if p.strip()])


def fix_paragraph_count(text: str, target: int) -> str:
    """Adjust paragraph count to match target by merging or splitting."""
    paras = [p.strip() for p in text.strip().split("\n\n") if p.strip()]
    if len(paras) == target:
        return text

    if len(paras) > target:
        # Too many: merge shortest adjacent pairs
        while len(paras) > target:
            shortest_idx = min(
                range(len(paras) - 1),
                key=lambda i: len(paras[i]) + len(paras[i + 1]),
            )
            paras[shortest_idx] = paras[shortest_idx] + " " + paras[shortest_idx + 1]
            paras.pop(shortest_idx + 1)
    elif len(paras) < target:
        # Too few: split longest paragraphs at sentence boundaries
        while len(paras) < target:
            longest_idx = max(range(len(paras)), key=lambda i: len(paras[i]))
            para = paras[longest_idx]
            mid = len(para) // 2
            best_pos = None
            for offset in range(mid):
                for pos in [mid + offset, mid - offset]:
                    if 0 < pos < len(para) - 1 and para[pos] in ".!?" and para[pos + 1] == " ":
                        best_pos = pos + 1
                        break
                if best_pos is not None:
                    break
            if best_pos is None:
                break  # can't split further
            part1 = para[:best_pos].strip()
            part2 = para[best_pos:].strip()
            if part1 and part2:
                paras[longest_idx] = part1
                paras.insert(longest_idx + 1, part2)
            else:
                break

    return "\n\n".join(paras)


def main():
    parser = argparse.ArgumentParser(description="Translate Persian/Arabic Baha'i texts into English")
    parser.add_argument("input", type=Path, help="Input file (.txt or .docx)")
    parser.add_argument("-o", "--output", type=Path, default=None, help="Output file (default: <input>.translated.txt)")
    parser.add_argument("--base-url", default=None, help="LLM endpoint (default: $TRANSLATE_BASE_URL or http://localhost:8317/v1)")
    parser.add_argument("--model", default=None, help="Model name (default: $TRANSLATE_MODEL or claude-opus-4-6)")
    parser.add_argument("--api-key", default=None, help="API key (default: $TRANSLATE_API_KEY or dummy-key)")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Error: {args.input} not found", file=sys.stderr)
        sys.exit(1)

    output_path = args.output or args.input.with_suffix(".translated.txt")

    # Read
    print("Reading input...", file=sys.stderr)
    source = read_input(args.input)
    if not source.strip():
        print("Error: input file is empty", file=sys.stderr)
        sys.exit(1)

    client = make_client(args)
    model = get_model(args)

    # Translate
    print("Translating...", file=sys.stderr)
    try:
        translation = translate(client, model, source)
    except Exception as e:
        print(f"Error: translation failed: {e}", file=sys.stderr)
        sys.exit(1)
    if not translation:
        print("Error: LLM returned empty translation", file=sys.stderr)
        sys.exit(1)

    # Verify
    print("Verifying...", file=sys.stderr)
    try:
        translation = verify(client, model, source, translation)
    except Exception as e:
        print(f"Warning: verification failed ({e}), using unverified translation", file=sys.stderr)

    # Post-process: paragraph count safety net
    target_paras = count_paragraphs(source)
    if target_paras > 0 and count_paragraphs(translation) != target_paras:
        translation = fix_paragraph_count(translation, target_paras)

    # Write
    output_path.write_text(translation, encoding="utf-8")
    print(f"Translation written to {output_path}", file=sys.stderr)


if __name__ == "__main__":
    main()

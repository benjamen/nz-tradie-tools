#!/bin/bash
# article-validate.sh <article_file>
# Validates a newly written article meets minimum quality standards.
# Exit 0 = PASS (safe to build and push)
# Exit 1 = FAIL (do NOT push — delete the file and do not publish)

ARTICLE="$1"
MIN_WORDS=2000

if [ -z "$ARTICLE" ] || [ ! -f "$ARTICLE" ]; then
    echo "FAIL: No article file provided or file not found: $ARTICLE"
    exit 1
fi

WORD_COUNT=$(wc -w < "$ARTICLE")
BASENAME=$(basename "$ARTICLE")

echo "Validating: $BASENAME"
echo "Word count: $WORD_COUNT (minimum: $MIN_WORDS)"

if [ "$WORD_COUNT" -lt "$MIN_WORDS" ]; then
    echo ""
    echo "❌ REJECTED — Article is too short ($WORD_COUNT words, minimum $MIN_WORDS)."
    echo "   Do NOT build or push this article."
    echo "   Delete the file and write a longer version with all required sections:"
    echo "     1. Introduction (200+ words, NZ context)"
    echo "     2. Background / Why This Matters in NZ (300+ words)"
    echo "     3. How-To or Main Content (600+ words, step-by-step or detailed advice)"
    echo "     4. Pricing / Costs in NZ (200+ words, real NZD figures)"
    echo "     5. Common Mistakes or FAQ (300+ words, 4–6 questions)"
    echo "     6. Conclusion + CTA (150+ words, mention Fastcrew/templates)"
    echo "     7. About NZ Tradie Tools footer (50+ words)"
    exit 1
fi

echo ""
echo "✅ PASSED — $WORD_COUNT words. Safe to build and push."
exit 0

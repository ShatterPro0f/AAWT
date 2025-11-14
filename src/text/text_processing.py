"""
Text Processing and Analysis Module
Provides comprehensive text analysis including word count, readability, complexity metrics.
"""

import re
import logging
from typing import Dict, List, Tuple, Any
from collections import Counter

logger = logging.getLogger(__name__)


class TextAnalyzer:
    """Analyzes text for various metrics and quality indicators."""
    
    def __init__(self):
        """Initialize text analyzer."""
        self.stop_words = {
            'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i',
            'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at',
            'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she',
            'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their'
        }
    
    def analyze_text(self, text: str) -> Dict[str, Any]:
        """
        Perform comprehensive text analysis.
        
        Args:
            text: Text to analyze
        
        Returns:
            Dictionary with analysis results
        """
        if not text or not text.strip():
            return self._empty_analysis()
        
        # Count metrics
        word_count = self._count_words(text)
        character_count = len(text)
        character_count_no_spaces = len(text.replace(' ', '').replace('\n', '').replace('\t', ''))
        sentence_count = self._count_sentences(text)
        paragraph_count = self._count_paragraphs(text)
        
        # Calculate averages
        avg_words_per_sentence = word_count / sentence_count if sentence_count > 0 else 0
        avg_chars_per_word = character_count_no_spaces / word_count if word_count > 0 else 0
        
        # Get words
        words = self._extract_words(text)
        unique_words = len(set(words))
        
        # Readability
        readability_score = self._calculate_readability(text, word_count, sentence_count)
        complexity_level = self._get_complexity_level(readability_score)
        grade_level = self._get_grade_level(readability_score)
        
        # Repeated words
        repeated_words = self._find_repeated_words(words)
        
        # Long sentences
        long_sentences = self._find_long_sentences(text)
        
        # Syllable count
        total_syllables = self._count_total_syllables(words)
        avg_syllables_per_word = total_syllables / word_count if word_count > 0 else 0
        
        # Reading time (assuming 250 words per minute)
        reading_time_minutes = word_count / 250
        
        return {
            'word_count': word_count,
            'character_count': character_count,
            'character_count_no_spaces': character_count_no_spaces,
            'sentence_count': sentence_count,
            'paragraph_count': paragraph_count,
            'average_words_per_sentence': round(avg_words_per_sentence, 2),
            'average_characters_per_word': round(avg_chars_per_word, 2),
            'unique_words': unique_words,
            'vocabulary_diversity': round(unique_words / word_count * 100, 2) if word_count > 0 else 0,
            'readability_score': round(readability_score, 2),
            'complexity_level': complexity_level,
            'grade_level': grade_level,
            'repeated_words': repeated_words,
            'long_sentences': long_sentences,
            'total_syllables': total_syllables,
            'average_syllables_per_word': round(avg_syllables_per_word, 2),
            'reading_time_minutes': round(reading_time_minutes, 2)
        }
    
    def _empty_analysis(self) -> Dict[str, Any]:
        """Return empty analysis result."""
        return {
            'word_count': 0,
            'character_count': 0,
            'character_count_no_spaces': 0,
            'sentence_count': 0,
            'paragraph_count': 0,
            'average_words_per_sentence': 0,
            'average_characters_per_word': 0,
            'unique_words': 0,
            'vocabulary_diversity': 0,
            'readability_score': 0,
            'complexity_level': 'N/A',
            'grade_level': 'N/A',
            'repeated_words': [],
            'long_sentences': [],
            'total_syllables': 0,
            'average_syllables_per_word': 0,
            'reading_time_minutes': 0
        }
    
    def _count_words(self, text: str) -> int:
        """Count words in text."""
        words = re.findall(r'\b\w+\b', text)
        return len(words)
    
    def _count_sentences(self, text: str) -> int:
        """Count sentences in text."""
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        return max(len(sentences), 1)  # At least 1 sentence
    
    def _count_paragraphs(self, text: str) -> int:
        """Count paragraphs in text."""
        paragraphs = text.split('\n\n')
        paragraphs = [p.strip() for p in paragraphs if p.strip()]
        return max(len(paragraphs), 1)  # At least 1 paragraph
    
    def _extract_words(self, text: str) -> List[str]:
        """Extract words from text."""
        words = re.findall(r'\b\w+\b', text.lower())
        return words
    
    def _calculate_readability(self, text: str, word_count: int, sentence_count: int) -> float:
        """
        Calculate Flesch Reading Ease score.
        Score ranges from 0-100, where higher is easier to read.
        """
        if word_count == 0 or sentence_count == 0:
            return 0
        
        words = self._extract_words(text)
        total_syllables = self._count_total_syllables(words)
        
        # Flesch Reading Ease formula
        score = 206.835 - 1.015 * (word_count / sentence_count) - 84.6 * (total_syllables / word_count)
        
        # Clamp between 0 and 100
        return max(0, min(100, score))
    
    def _get_complexity_level(self, readability_score: float) -> str:
        """Get complexity level from readability score."""
        if readability_score >= 80:
            return 'Simple'
        elif readability_score >= 60:
            return 'Moderate'
        else:
            return 'Complex'
    
    def _get_grade_level(self, readability_score: float) -> str:
        """Get grade level equivalent from readability score."""
        if readability_score >= 90:
            return '5th Grade'
        elif readability_score >= 80:
            return '6th Grade'
        elif readability_score >= 70:
            return '7th-8th Grade'
        elif readability_score >= 60:
            return '9th-10th Grade'
        elif readability_score >= 50:
            return '11th-12th Grade'
        elif readability_score >= 30:
            return 'College'
        else:
            return 'College Graduate'
    
    def _count_syllables(self, word: str) -> int:
        """Estimate syllable count for a word."""
        word = word.lower().strip()
        if len(word) <= 3:
            return 1
        
        # Remove trailing 'e'
        if word.endswith('e'):
            word = word[:-1]
        
        # Count vowel groups
        vowels = 'aeiouy'
        syllable_count = 0
        previous_was_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not previous_was_vowel:
                syllable_count += 1
            previous_was_vowel = is_vowel
        
        # Ensure at least 1 syllable
        return max(1, syllable_count)
    
    def _count_total_syllables(self, words: List[str]) -> int:
        """Count total syllables in word list."""
        return sum(self._count_syllables(word) for word in words)
    
    def _find_repeated_words(self, words: List[str], threshold: int = 3) -> List[Tuple[str, int]]:
        """
        Find words that appear frequently.
        
        Args:
            words: List of words
            threshold: Minimum count to be considered repeated
        
        Returns:
            List of (word, count) tuples, sorted by count descending
        """
        # Filter out stop words
        meaningful_words = [w for w in words if w not in self.stop_words and len(w) > 3]
        
        # Count occurrences
        word_counts = Counter(meaningful_words)
        
        # Filter by threshold and sort
        repeated = [(word, count) for word, count in word_counts.items() if count >= threshold]
        repeated.sort(key=lambda x: x[1], reverse=True)
        
        return repeated[:20]  # Top 20
    
    def _find_long_sentences(self, text: str, threshold: int = 25) -> List[Dict[str, Any]]:
        """
        Find sentences that exceed word count threshold.
        
        Args:
            text: Text to analyze
            threshold: Maximum words per sentence
        
        Returns:
            List of sentence info dictionaries
        """
        sentences = re.split(r'[.!?]+', text)
        long_sentences = []
        
        for i, sentence in enumerate(sentences, 1):
            sentence = sentence.strip()
            if sentence:
                word_count = len(re.findall(r'\b\w+\b', sentence))
                if word_count > threshold:
                    # Truncate for display
                    display = sentence[:100] + '...' if len(sentence) > 100 else sentence
                    long_sentences.append({
                        'sentence_number': i,
                        'word_count': word_count,
                        'text': display
                    })
        
        return long_sentences[:10]  # Top 10
    
    def check_consistency(self, text: str) -> Dict[str, List]:
        """
        Check for consistency issues in text.
        
        Returns:
            Dictionary with potential inconsistencies
        """
        words = self._extract_words(text)
        
        # Find potential name variations (capitalized words)
        capitalized = re.findall(r'\b[A-Z][a-z]+\b', text)
        name_variations = self._find_similar_names(capitalized)
        
        return {
            'name_variations': name_variations,
            'capitalization_issues': self._find_capitalization_issues(text)
        }
    
    def _find_similar_names(self, names: List[str]) -> List[Tuple[str, List[str]]]:
        """Find similar name variations."""
        # Simple implementation - could be enhanced with edit distance
        name_groups = {}
        
        for name in set(names):
            key = name.lower()[:3]  # Group by first 3 letters
            if key not in name_groups:
                name_groups[key] = []
            name_groups[key].append(name)
        
        # Return groups with multiple variations
        variations = []
        for group in name_groups.values():
            if len(set(group)) > 1:
                variations.append((group[0], list(set(group))))
        
        return variations
    
    def _find_capitalization_issues(self, text: str) -> List[str]:
        """Find potential capitalization inconsistencies."""
        # Find words that appear both capitalized and lowercase
        words = re.findall(r'\b\w+\b', text)
        word_forms = {}
        
        for word in words:
            lower = word.lower()
            if lower not in word_forms:
                word_forms[lower] = set()
            word_forms[lower].add(word)
        
        # Find words with multiple forms
        issues = []
        for lower, forms in word_forms.items():
            if len(forms) > 1 and len(lower) > 3:
                issues.append(f"{lower}: {', '.join(sorted(forms))}")
        
        return issues[:20]  # Top 20
    
    def analyze_style(self, text: str, target_tone: str = 'Professional', 
                     target_pov: str = 'Third Limited') -> Dict[str, Any]:
        """
        Analyze text style and tone.
        
        Args:
            text: Text to analyze
            target_tone: Target tone
            target_pov: Target point of view
        
        Returns:
            Style analysis results
        """
        words = self._extract_words(text)
        
        # Detect POV
        first_person = len([w for w in words if w in ['i', 'me', 'my', 'mine', 'we', 'us', 'our']])
        second_person = len([w for w in words if w in ['you', 'your', 'yours']])
        third_person = len([w for w in words if w in ['he', 'she', 'they', 'him', 'her', 'them']])
        
        total_pronouns = first_person + second_person + third_person
        
        detected_pov = 'Unknown'
        if total_pronouns > 0:
            if first_person / total_pronouns > 0.5:
                detected_pov = 'First Person'
            elif second_person / total_pronouns > 0.5:
                detected_pov = 'Second Person'
            elif third_person / total_pronouns > 0.5:
                detected_pov = 'Third Person'
        
        # Detect tone indicators
        formal_words = len([w for w in words if w in ['furthermore', 'moreover', 'consequently', 'therefore']])
        casual_words = len([w for w in words if w in ['gonna', 'wanna', 'yeah', 'ok', 'cool']])
        
        pov_matches = detected_pov.startswith(target_pov.split()[0])
        
        return {
            'detected_pov': detected_pov,
            'target_pov': target_pov,
            'pov_matches': pov_matches,
            'first_person_count': first_person,
            'second_person_count': second_person,
            'third_person_count': third_person,
            'formal_indicators': formal_words,
            'casual_indicators': casual_words,
            'tone_assessment': 'Formal' if formal_words > casual_words else 'Casual'
        }

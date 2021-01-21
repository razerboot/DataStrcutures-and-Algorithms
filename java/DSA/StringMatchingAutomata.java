
import java.util.*;

public class StringMatchingAutomata {

	private String pattern;
	private int[][] automata;

	public StringMatchingAutomata(String pattern) {
		this.pattern = pattern;
		constructAutomata(pattern);
	}

	private void constructAutomata(String pattern) {
		int m = pattern.length();
		Set<Character> inp = new HashSet<Character>();
		for (int i=0; i <= m - 1; i++)
			inp.add(pattern.charAt(i));
		List<Character> charList = new ArrayList<Character>(inp);
		int n = charList.size();
		automata = new int[m + 1][n];
		for (int i = 0; i <= m; i++) {
			for (int j = 0; j < n; j++) {
				automata[i][j] = findLongestPrefixInPatternWhichIsSuffix(pattern, i, charList.get(j));
			}
		}
	}

	private int findLongestPrefixInPatternWhichIsSuffix(String pattern, int p, char a) {
		int m = pattern.length();
		int n = Math.min(p + 1, m);
		for (int i = n; i > 0; i--) {
			for (int j = 0; j < i; j++) {
				if (j != i - 1 && pattern.charAt(j) != pattern.charAt(p - i + 1 + j))
					break;
				else if (j == i - 1 && pattern.charAt(j) != a)
					break;
				else if (j == i - 1)
					return i;
			}
		}
		return 0;
	}
}
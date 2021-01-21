import java.util.*;

public class LongestUniqueSubstring {

	private String s;

	public LongestUniqueSubstring(String s) {
		this.s = s;
	}

	public int findLongestUniqueSubstring() {
		int n = s.length();
		Set<Character> prevPos = new HashSet<Character>();
		int uStart = 0;
		int maxLen = 0;
		prevPos.add(s.charAt(0));
		for (int i = 1; i < n; i++) {
			while (prevPos.contains(s.charAt(i))) {
				prevPos.remove(s.charAt(uStart));
				uStart++;
			}
			if (!prevPos.contains(s.charAt(i))) {
				prevPos.add(s.charAt(i));
				maxLen = Math.max(maxLen, i - uStart + 1);
			}
		}
		return maxLen;
	}

	public static void main(String[] args) {
		LongestUniqueSubstring lu = new LongestUniqueSubstring("abcc");
		System.out.println(lu.findLongestUniqueSubstring());
	} 
}
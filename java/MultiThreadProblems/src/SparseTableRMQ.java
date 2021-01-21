import java.lang.Math;
import java.util.*;
public class SparseTableRMQ implements RMQ {
    int[] iA;
    int[][] st;

    public SparseTableRMQ(int[] inp) {
        iA = inp;
        buildSparseTree();
    }

    private void buildSparseTree() {
        int m = iA.length;
        int n = getLog2(m);
        st = new int[n + 1][m];
        System.arraycopy(iA, 0, st[0], 0, m);
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j + pow(2, i) - 1 < m; j++) {
                st[i][j] = Math.min(st[i - 1][j], st[i - 1][j + pow(2, i - 1)]);
            }
        }
    }

    @Override
    public Integer getMin(int l, int r) {
        int k = r - l + 1;
        int lk = getLog2(k);
        int p = pow(2, lk);
        return Math.min(st[lk][l], st[lk][r - p + 1]);
    }

    private int pow(int i, int j) {
        return (int) Math.pow(i, j);
    }

    public static void main(String[] args) {
        SparseTableRMQ st = new SparseTableRMQ(new int[1]);
        System.out.println(st.getLog2(64));
    }

    private int getLog2(int n) {
        int log = 0;
        while (n > 1) {
            n = n >> 1;
            log++;
        }
        return log;
    }
}

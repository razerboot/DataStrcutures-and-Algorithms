import java.lang.*;
public class SegmentTreeRMQ implements RMQ {

    int[] in;
    int[] st;

    public SegmentTreeRMQ(int[] in) {
        this.in = in;
        int n = in.length;
        int ceil2 = getCeil2Power(n);
        int N = pow(2, ceil2);
        st = new int[2 * N];
        buildSegTree(st, in, 1, 0, n - 1);
    }

    private void buildSegTree(int[] st, int[] in, int p, int l, int r) {
        if (l == r) {
            st[p] = in[l];
            return;
        }
        int mid = (l + r) / 2;
        buildSegTree(st, in, 2 * p, l, mid);
        buildSegTree(st, in, 2 * p + 1, mid + 1, r);
        st[p] = Math.min(st[2 * p], st[2 * p + 1]);
    }

    private int getCeil2Power(int i) {
        int ceil2 = 1;
        int log = 0;
        while (ceil2 < i) {
            ceil2 *= 2;
            log++;
        }
        return log;
    }

    private int getFloor2Power(int i) {
        int floor2 = 0;
        while (i > 1) {
            i = i / 2;
            floor2++;
        }
        return floor2;
    }

    private int pow(int x, int y) {
        return (int) Math.pow(x, y);
    }

    @Override
    public Integer getMin(int l, int r) {
        return getMin(l, r, 0, in.length - 1, 1);
    }

    private Integer getMin(int x, int y, int l, int r, int p) {
        // current node range is within input range
        if (x <= l && r <= y)
            return st[p];
        // no overlap
       if (l > y || r < x)
           return -1;

       int mid = (l + r) / 2;
       int lMin = getMin(x, y, l, mid, 2 * p);
       int rMin = getMin(x, y, mid + 1, r, 2 * p + 1);
       if (lMin == -1)
           return rMin;
       if (rMin == -1)
           return lMin;
       return Math.min(lMin, rMin);
    }
}

public class RMQTester {
    public static void main(String[] args) {
        RMQ st = new SegmentTreeRMQ(new int[]{45, 4, 7, 9, 8, 1, 3, 2, 5});
        System.out.println(st.getMin(3, 3));
        System.out.println(st.getMin(1, 4));
        System.out.println(st.getMin(3, 7));
        System.out.println(st.getMin(2, 5));
        System.out.println(st.getMin(0, 8));

        RMQ st1 = new SparseTableRMQ(new int[]{45, 4, 7, 9, 8, 1, 3, 2, 5});
        System.out.println(st1.getMin(3, 3));
        System.out.println(st1.getMin(1, 4));
        System.out.println(st1.getMin(3, 7));
        System.out.println(st1.getMin(2, 5));
        System.out.println(st1.getMin(0, 8));
    }
}

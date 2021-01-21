import java.util.Collections;
import java.util.List;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.atomic.AtomicInteger;

public class Node {
    private String id;
    private String url;
    private List<Node> inIdRelation;
    private AtomicInteger outCount;

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Node node = (Node) o;

        if (!outCount.equals(node.outCount)) return false;
        return inCount.equals(node.inCount);
    }

    @Override
    public int hashCode() {
        int result = outCount.hashCode();
        result = 31 * result + inCount.hashCode();
        return result;
    }

    private Integer inCount;

    public Node(String id, String url, Integer outIdRelation, List<Node> inIdRelation) {
        this.id = id;
        this.url = url;
        this.inIdRelation = inIdRelation != null ? inIdRelation : Collections.EMPTY_LIST;
        this.outCount = new AtomicInteger(outIdRelation);
    }

    public void execute(CountDownLatch countDownLatch) {
        execute();
        for (Node n: inIdRelation) {
            Node parent = n;
            parent.reduceChildCount();
            parent.startIfRequired(countDownLatch);
        }
    }

    public void execute() {
        System.out.println(url + " executed");
    }

    public void startIfRequired(CountDownLatch countDownLatch) {
        if (outCount.get() == 0) {
            synchronized (this) {
                if (outCount.get() == 0) {
                    new Thread(new JobExecutor(this, countDownLatch)).start();
                    outCount.decrementAndGet();
                }
            }
        }
    }

    private void reduceChildCount() {
        this.outCount.decrementAndGet();
    }
}

import java.util.concurrent.CountDownLatch;

public class JobExecutor implements Runnable {

    Node node;
    CountDownLatch countDownLatch;

    public JobExecutor(Node node, CountDownLatch countDownLatch) {
        this.node = node;
        this.countDownLatch = countDownLatch;
    }

    public void run() {
        node.execute(countDownLatch);
        countDownLatch.countDown();
    }
}

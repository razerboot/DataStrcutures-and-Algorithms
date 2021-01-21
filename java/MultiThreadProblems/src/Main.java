import java.util.Arrays;
import java.util.Collections;
import java.util.concurrent.CountDownLatch;

public class Main {

    public static void main(String[] args) {
        System.out.println("Hello World!");
        CountDownLatch countDownLatch = new CountDownLatch(4);
        Node node = new Node("1", "a", 2, null);
        Node node1 = new Node("2", "b", 1, Collections.singletonList(node));
        Node node2 = new Node("3", "c", 1, Collections.singletonList(node));
        Node node3 = new Node("4", "d", 0, Arrays.asList(node1, node2));
        new Thread(new JobExecutor(node3, countDownLatch)).start();
        try {
            countDownLatch.await();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("complete");
    }


}

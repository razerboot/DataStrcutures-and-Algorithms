import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.lang.Math;

public class SquareCounting2017 {


	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		br.readLine();
		long mod = 1000000007;
		for (String inp = br.readLine(); inp != null; inp = br.readLine()) {
			String[] dim = inp.split(" ");
			long m = Math.max(Integer.parseInt(dim[0]), Integer.parseInt(dim[1]));
			long n = Math.min(Integer.parseInt(dim[0]), Integer.parseInt(dim[1]));
			m = m % mod;
			n = n % mod;
			long parallelSquares = (((((n * (n - 1)) % mod) * ((3 * m - n - 1) % mod)) % mod) * power(6, mod - 2, mod)) % mod;
			System.out.println(parallelSquares);
		}
	}

	    // To compute x^y under modulo m 
    static long power(long x, long y, long m)  
    {
        if (y == 0) 
            return 1; 
          
        long p = power(x, y / 2, m) % m; 
        p = (p * p) % m; 
      
        if (y % 2 == 0) 
            return p; 
        else
            return (x * p) % m; 
    }

}
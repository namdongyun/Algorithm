import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();
        int index = 0;
        int n = 1;

        while (index < str.length()) {
            String nStr = String.valueOf(n);

            for (int i=0; i<nStr.length(); i++) {
                if (index < str.length() && str.charAt(index) == nStr.charAt(i)) {
                    index++;
                }
            }
            n++;
        }
        System.out.println(n-1);
    }
}

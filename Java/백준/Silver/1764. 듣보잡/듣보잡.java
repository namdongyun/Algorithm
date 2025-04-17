import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] inputs = br.readLine().split(" ");
        int n = Integer.parseInt(inputs[0]);        // 듣도 못한 사람의 수
        int m = Integer.parseInt(inputs[1]);        // 보도 못한 사람의 수

        HashSet<String> setN = new HashSet<>();     // 듣도 못한 사람 리스트
        TreeSet<String> result = new TreeSet<>();   // 듣보잡

        for (int i=0; i<n; i++) {   // 듣도 못한 사람 입력 받기
            setN.add(br.readLine());
        }
        for (int j=0; j<m; j++) {   // 보도 못한 사람 입력 받기
            String name = br.readLine();
            if (setN.contains(name)) {
                result.add(name);
            }
        }
        System.out.println(result.size());
        for (String s : result) {
            System.out.println(s);
        }
    }
}
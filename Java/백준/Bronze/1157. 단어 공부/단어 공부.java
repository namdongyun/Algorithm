import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 입력한 단어 받기
        String str = br.readLine();

        int max = -1;
        char ch = '?';

        // 입력한 글자 하나씩 해당 아스키 코드 값 - 'a' or 'A' 하여 int 배열에 추가
        int[] result = new int[26];

        for (int i=0; i<str.length(); i++) {
            if (str.charAt(i) - 'a' >= 0) {
                result[str.charAt(i) - 'a']++;
            } else {
                result[str.charAt(i) - 'A']++;
            }
        }
        
        // result 배열에서 max 값 찾기
        for (int j=0; j<result.length; j++) {
            if (max < result[j]) {
                max = result[j];
                ch = (char)(j + 'A');
            } else if (max == result[j]) {
                ch = '?';
            }
        }
        System.out.println(ch); // 대문자 max 값 철자 출력
    }
}
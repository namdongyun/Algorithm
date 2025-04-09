import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 입력한 단어 받기
        String str = br.readLine();

        int max = 0;
        int count = 0;

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
            if (result[max] < result[j]) max = j;
        }

        for (int k=0; k<result.length; k++) {
            if (result[max] == result[k]) count++;
        }

        if (count > 1) {
            System.out.print("?");  // max 값 여러개 일 경우 ? 출력
        } else {
            System.out.println((char) (max + 'A')); // 대문자 max 값 철자 출력
        }
    }
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputStr = "";   // 테스트 케이스 입력받는 변수

        while(true) {
            inputStr = br.readLine();   // 테스트 케이스 입력받기
            if (inputStr.equals("end")) break;   // end 입력시 종료

            if (checkPassword(inputStr)) {
                System.out.println("<" + inputStr + "> is acceptable.");
            } else {
                System.out.println("<" + inputStr + "> is not acceptable.");
            }
        }
    }

    public static boolean checkPassword(String inputStr) {
        char ch = ' ';      // 철자
        char prevCh = ' ';  // 이전 철자
        int totalVo = 0;    // 누적 모음 개수
        int vo = 0;         // 연속 모음 개수
        int co = 0;         // 연속 자음 개수

        for (int i=0; i<inputStr.length(); i++) {
            ch = inputStr.charAt(i);
            if (ch==prevCh) {   // 글자 연속 두번 예외
                if (ch!='e' && ch!='o') return false;
            }

            if (ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u') {  // 모음 자음 연속 개수
                totalVo++;  // 누적 모음 개수 ++
                vo++;       // 연속 모음 개수 ++
                co = 0;     // 연속 자음 개수 초기화
            } else {
                co++;       // 연속 자음 개수 ++
                vo = 0;     // 연속 모음 개수 초기화
            }

            if (vo >= 3 || co >= 3) {
                return false;
            }

            prevCh = ch;
        }

        if (totalVo >= 1) {
            return true;
        }
        return false;
    }
}

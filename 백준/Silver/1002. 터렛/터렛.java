import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for (int i = T; i > 0; i--) {
            int x1 = sc.nextInt();
            int y1 = sc.nextInt();
            int r1 = sc.nextInt();

            int x2 = sc.nextInt();
            int y2 = sc.nextInt();
            int r2 = sc.nextInt();

            System.out.println(count(x1, y1, r1, x2, y2, r2));
        }

    }

    public static int count(int x1, int y1, int r1, int x2, int y2, int r2) {
        int radius_pow = (int) Math.pow((x2 - x1), 2) + (int) Math.pow((y2 - y1), 2); // 두 점 사이 간격의 제곱

        if (x1 == x2 && y1 == y2 && r1 == r2) {
            return -1;
        } else if (radius_pow == (int) Math.pow(r2 - r1, 2)) { // 두 원의 반지름 길이의 차 = 두 점 사이 간격일 때 (두 원이 내부 접점)
            return 1;
        } else if (radius_pow == (int) Math.pow(r2 + r1, 2)) { // 두 원이 외부 접점
            return 1;
        } else if (x1 == x2 && y1 == y2 && r1 != r2) { // 두 점이 같은 위치이며, 반지름이 다를 경우
            return 0;
        } else if (radius_pow < (int) Math.pow(r2 - r1, 2)) {
            return 0;
        } else if (radius_pow > (int) Math.pow(r2 + r1, 2)) {
            return 0;
        } else {
            return 2; // 두 원이 겹쳐 2개의 접점이 생김
        }
    }
}
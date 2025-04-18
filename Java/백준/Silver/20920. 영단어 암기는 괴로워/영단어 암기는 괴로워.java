import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] inputs = br.readLine().split(" ");
        int n = Integer.parseInt(inputs[0]);
        int m = Integer.parseInt(inputs[1]);

        Map<String, Integer> wordMap = new HashMap<>(n);

        for (int i=0; i<n; i++) {   // N개 단어 받기
            String word = br.readLine();
            if (word.length() >= m) {
                wordMap.put(word, wordMap.getOrDefault(word, 0) + 1);
            }
        }

        List<String> wordList = new ArrayList<>(wordMap.keySet());

        wordList.sort((w1, w2) -> {
            int freq1 = wordMap.get(w1);
            int freq2 = wordMap.get(w2);

            if (freq1 != freq2) return freq2 - freq1;
            if (w1.length() != w2.length()) return w2.length() - w1.length();
            return w1.compareTo(w2);
        });

        StringBuilder sb = new StringBuilder();
        for (String word : wordList) {
            sb.append(word).append('\n');
        }
        bw.write(sb.toString());

        bw.flush();
        bw.close();
    }
}
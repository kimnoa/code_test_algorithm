class Solution {
    public int solution(int n, int w, int num) {
        int answer = 0;
        int q1 = (n-1) / w;
        int r1 = (n-1) % w;
        int q2 = (num-1) / w;
        int r2 = (num-1) % w;
        
        System.out.printf("%d %d %d %d", q1, r1, q2, r2);
        
        if ((q1-q2) % 2 > 0) {
            if (r1+r2>=(w-1))
                return q1-q2+1;
            return q1-q2;
        }
        if (r1>=r2)
            return q1-q2+1;
        return q1-q2;
    }
}
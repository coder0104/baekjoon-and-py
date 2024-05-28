#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<math.h>

using namespace std;

int digits[19], len, K;
long long N;
string cache[1 << 11][19][2];

void calDigit() {
	long long num = N;

	while (num > 0) {
		digits[len++] = num % 10;
		num /= 10;
	}

	for (int s = 0, e = len - 1; s < e; s++, e--) {
		int tmp = digits[s];
		digits[s] = digits[e];
		digits[e] = tmp;
	}
}

string ans(int idx, int taken, int takenCnt, int pass) {
	if (idx == len)
		return takenCnt == K ? "" : "111111111111111111111111111111111";

	string& ret = cache[taken][idx][pass];

	if (!(ret.empty()))
		return ret;
	
	for (int d = (pass == 1 ? 0 + (idx == 0) : digits[idx]); d < 10 + (idx == 0); d++) {
		int newPass = pass || d > digits[idx];
		
		if (d == 10) {
			len += 1;
			ret = to_string(1) + ans(idx + 1, taken | (1 << 1), takenCnt + !(taken & (1 << 1)), 1);
		}
		else
			ret = to_string(d) + ans(idx + 1, taken | (1 << d), takenCnt + !(taken & (1 << d)), newPass);
		
		if (ret.size() < 30)
			return ret;
	}
	return ret;
}

int main(void) {
	int p = 0;

	cin >> N >> K;
	
	calDigit();
	
	if (len < K) {
		len = K;
		p = 1;
	}

	cout << ans(0, 0, 0, p);
	
	return 0;
}
#include <stdio.h>


void _recursive_score(int cur_score, int max_score, int td8, int td7, int td6, int fg3, int sf2, int last_score);

int main() {

    int max_score = 25;
    _recursive_score(0, max_score, 0, 0, 0, 0, 0, 1);
    return 0;
}

void _recursive_score(int cur_score, int max_score, int td8, int td7, int td6, int fg3, int sf2, int last_score) {
    if (cur_score == max_score) {
        printf("%d TD + 2pt, %d TD + FG, %d TD, %d 3pt FG, %d Safety\n", td8, td7, td6, fg3, sf2);
    }
    if (cur_score + 2 <= max_score && last_score <= 2) {
        _recursive_score(cur_score + 2, max_score, td8, td7, td6, fg3, sf2 + 1, 2);
    }
    if (cur_score + 3 <= max_score && last_score <= 3) {
        _recursive_score(cur_score + 3, max_score, td8, td7, td6, fg3 + 1, sf2, 3);
    }
    if (cur_score + 6 <= max_score && last_score <= 6) {
        _recursive_score(cur_score + 6, max_score, td8, td7, td6 + 1, fg3, sf2, 6);
    }
    if (cur_score + 7 <= max_score && last_score <= 7) {
        _recursive_score(cur_score + 7, max_score, td8, td7 + 1, td6, fg3, sf2, 7);
    }
    if (cur_score + 8 <= max_score && last_score <= 8) {
        _recursive_score(cur_score + 8, max_score, td8 + 1, td7, td6, fg3, sf2, 8);
    }
}
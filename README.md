# 한국어문회 등급별 선정한자 CSV 데이터셋

[사단법인 한국어문회](https://www.hanja.re.kr/)에서 분류한 급수별 한자 데이터셋입니다. 공식 홈페이지의 학습자료 / 기타자료에 업로드된 Xls 파일을 CSV 파일로 변환하여 제공합니다.

데이터의 저작권은 한국어문회에 있습니다. 데이터의 오류나 문제가 있을 경우 [이슈](https://github.com/rycont/hanja-grade-dataset/issues)를 남겨주시면 확인 후 수정하겠습니다.

## 데이터 다운로드

[hanja.csv](https://github.com/rycont/kta-hanja-grade-dataset/blob/main/hanja.csv)

## 데이터 예시

| main_sound | level | hanja | meaning | radical | strokes | total_strokes |
|------------|-------|-------|---------|---------|---------|---------------|
| 가         | 7급Ⅱ  | 家    | [[['집'], ['가']]] | 宀     | 7       | 10            |
| 가         | 7급   | 歌    | [[['노래'], ['가']]] | 欠   | 10      | 14            |
| 가         | 5급Ⅱ  | 價    | [[['값'], ['가']]] | 人     | 13      | 15            |

## 데이터 구성

### 급수별 한자 갯수

| 급수 | 갯수 |
|-----|------|
| 8급 | 50   |
| 7급 | 50   |
| 7급Ⅱ | 50   |
| 6급 | 75   |
| 6급Ⅱ | 75   |
| 5급 | 100  |
| 5급Ⅱ | 100  |
| 4급 | 250  |
| 4급Ⅱ | 250  |
| 3급 | 317  |
| 3급Ⅱ | 500  |
| 2급 | 538  |
| 1급 | 1145 |
| 특급 | 1150 |
| 특급Ⅱ | 1328 |

### 필드

```typescript
interface Hanja {
    // 대표 독음
    main_sound: string;

    // 한국어문회 분류 급수
    level: string;

    // 한자
    hanja: string;

    // 의미
    meaning: Meaning[];

    // 부수
    radical: string;

    // 획수
    strokes: number;

    // 총 획수
    total_strokes: number;
}

type Meaning = [
    // 의미
    string[],

    // 한자 독음
    string[]
]
```

---

Made with ❤️ by [rycont](https://bento.me/3)

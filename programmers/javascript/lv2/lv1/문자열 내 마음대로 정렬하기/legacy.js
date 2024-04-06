const ALPHABET_DICT = {
  a: 1,
  b: 2,
  c: 3,
  d: 4,
  e: 5,
  f: 6,
  g: 7,
  h: 8,
  i: 9,
  j: 10,
  k: 11,
  l: 12,
  m: 13,
  n: 14,
  o: 15,
  p: 16,
  q: 17,
  r: 18,
  s: 19,
  t: 20,
  u: 21,
  v: 22,
  w: 23,
  x: 24,
  y: 25,
  z: 26,
};

function solution(strings, n) {
  const sortedString = strings.sort((a, b) => {
    if (ALPHABET_DICT[a[n]] !== ALPHABET_DICT[b[n]])
      return ALPHABET_DICT[a[n]] - ALPHABET_DICT[b[n]];
    if (a === b) return 0;
    for (let i = 0; i < Math.min(a.length, b.length); i++) {
      if (ALPHABET_DICT[a[i]] !== ALPHABET_DICT[b[i]])
        return ALPHABET_DICT[a[i]] - ALPHABET_DICT[b[i]];
    }
    return a.length - b.length;
  });

  return sortedString;
}

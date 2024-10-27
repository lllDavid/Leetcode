/**
 * @return {Generator<number>}
 */
var fibGenerator = function* () {
    let a = 0;
    let b = 1;
    let c;

    yield 0
    yield 1

    while (true) {
        c = a + b
        a = b
        b = c
        yield c;
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */
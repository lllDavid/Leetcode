/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = functions => new Promise((resolve, reject) => {
    if (functions.length === 0) return resolve([]);

    const results = [], total = functions.length;
    let count = 0;

    functions.forEach((fn, i) => {
        fn().then(val => {
            results[i] = val;
            if (++count === total) resolve(results);
        }).catch(err => reject(err));
    });
});


/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */
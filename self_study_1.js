//1
    for (let j =1 ; j < 10 ; j=j+2) {
        console.log('*'.repeat(j))
}

//2-1 다음 배열에서 '라'를 모두 제거하세요. indexOf와 splice 사용
const arr = ['가','라','다','라','마','라']
arr.indexOf('라')
arr.splice(1,1)
arr.splice(2,1)
arr.splice(3,1)
console.log(arr)

//2-2
const array = ['가','라','다','라','마','라']
while (array.indexOf('라')>-1) {
    array.splice(array.indexOf('라',1))
}
console.log(array)

//3


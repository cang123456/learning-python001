
// 辅助函数：等待元素出现（通用万能）
function waitForElement(selector) {
    return new Promise(resolve => {
        if (document.querySelector(selector)) {
            return resolve(document.querySelector(selector));
        }
        const observer = new MutationObserver(mutations => {
            if (document.querySelector(selector)) {
                resolve(document.querySelector(selector));
                observer.disconnect();
            }
        });
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    });
}

function s2() {//填写成绩和评语


    // 填写成绩
    const totalScore = document.querySelector('.totalScore');
    const scoreInput = totalScore.querySelector('input');
    scoreInput.click()
    scoreInput.value = scoreInput.getAttribute('data')

    setTimeout(1000);
    // 填写评语
    let piny = ["ok", "不错", "很好", "good"]
    const text1 = document.querySelector('.kark_comment_text'); //评语展示框
    text1.click()
    text1.innerHTML = ""
    const text2 = document.querySelector('body.view p');
    text2.innerText=piny[Math.floor(Math.random() * piny.length)]

}
function s1(){ //进入互评页面
    const btns = document.querySelectorAll('.dataBody_piyue a');
    for(let i = 0; i < btns.length; i++){
        btns[i].click()
        s2()
    }
}
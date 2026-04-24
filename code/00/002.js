




(function() {
    'use strict';

    let x = 3;
    // Your code here...
    // 在页面创建按钮
    let bt = document.createElement("button");
    bt.innerHTML = "一键互评";
    bt.onclick = s1
    // 设置位置，不随页面滚动
    bt.style.position="fixed";
    bt.style.left=0;
    bt.style.top="50%";
    //设置 z-index 值，保证按钮在最上层
    bt.style.zIndex=3333;
    document.body.appendChild(bt);
})();




// 等待主页面元素的通用函数
function waitForMainElement(selector, timeout = 10000) {
    return new Promise((resolve, reject) => {
        const timer = setTimeout(() => reject(new Error(`超时未找到主页面元素：${selector}`)), timeout);
        if (document.querySelector(selector)) {
            clearTimeout(timer);
            return resolve(document.querySelector(selector));
        }
        const observer = new MutationObserver(() => {
            const el = document.querySelector(selector);
            if (el) {
                clearTimeout(timer);
                resolve(el);
                observer.disconnect();
            }
        });
        observer.observe(document.body, { childList: true, subtree: true });
    });
}

// 等待iframe内部元素的函数
function waitForIframeElement(iframe, selector, timeout = 10000) {
    return new Promise((resolve, reject) => {
        const timer = setTimeout(() => reject(new Error(`超时未找到iframe元素：${selector}`)), timeout);
        const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
        if (iframeDoc.querySelector(selector)) {
            clearTimeout(timer);
            return resolve(iframeDoc.querySelector(selector));
        }
        const observer = new MutationObserver(() => {
            const el = iframeDoc.querySelector(selector);
            if (el) {
                clearTimeout(timer);
                resolve(el);
                observer.disconnect();
            }
        });
        observer.observe(iframeDoc.body, { childList: true, subtree: true });
    });
}

async function s2() {
    try {
        // ======================
        // 1. 填写成绩（在主页面找）
        // ======================
        console.log('⏳ 等待成绩区域加载...');
        const totalScore = await waitForMainElement('.totalScore');
        console.log('✅ 找到成绩区域');

        const scoreInput = totalScore.querySelector('input');
        const maxScore = scoreInput.getAttribute('data');
        scoreInput.value = maxScore;
        scoreInput.dispatchEvent(new Event('input'));
        scoreInput.dispatchEvent(new Event('blur'));
        console.log('✅ 成绩填写完成');

        // ======================
        // 2. 填写评语（在iframe里找）
        // ======================
        console.log('⏳ 等待评语编辑器加载...');
        const piny = ["ok", "不错", "很好", "good"];

        // 点击评语框
        const text1 = await waitForMainElement('.kark_comment_text');
        text1.click();

        // 找到iframe
        const iframe = await waitForMainElement('iframe[src*="editor"], iframe[class*="ueditor"]');
        console.log('✅ 找到评语编辑器iframe');

        // 等待iframe里的p标签
        const text2 = await waitForIframeElement(iframe, 'body.view p');
        console.log('✅ 找到评语输入框');

        // 写入评语
        text2.innerHTML = '';
        text2.innerText = piny[Math.floor(Math.random() * piny.length)];
        text2.dispatchEvent(new Event('input', { bubbles: true }));
        console.log('✅ 评语填写完成');

    } catch (err) {
        console.error('❌ 执行失败：', err.message);
    }
}

function s1(){ //进入互评页面
    const btns = document.querySelectorAll('.dataBody_piyue a');
    btns[0].click()
    s2()
}
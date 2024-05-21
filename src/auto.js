
function getAllAnswerSections() {
    return  document.getElementsByClassName('ans-form');
}
function getSafeAnswer(answerSection) {
    const inputs = answerSection.getElementsByTagName('input');
    const first = inputs?.first;
    return first;
}

function submitForm() {
    document.getElementById('btn-regist').click();
    setTimeout(() => {
        document.getElementById('btn-confirm-ok').click();
      }, 1000);
}


function main() {
    const answerForms = getAllAnswerSections();
    for(const form of answerForms) {
        const safe = getSafeAnswer(form);
        safe?.click();
    }
    submitForm();
}

main();
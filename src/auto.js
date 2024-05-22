
function getAllAnswerSections() {
    return  document.getElementsByClassName('ans-form');
}
function getSafeAnswer(answerSection) {
    const inputs = [...answerSection.getElementsByTagName('input')];
    if(inputs.length > 0) {
        const first = inputs[0];
        return first;    
    }
    return null;
}

async function submitForm() {
    document.getElementById('btn-regist').click();
    await new Promise(resolve => setTimeout(resolve, 3000)) 
    document.getElementById('btn-confirm-ok').click();
    await new Promise(resolve => setTimeout(resolve, 3000)) 
}


async function main() {
    const answerForms = getAllAnswerSections();
    for(const form of answerForms) {
        const safe = getSafeAnswer(form);
        safe?.click();
    }
    await submitForm();
}

main();
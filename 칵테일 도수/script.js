document.addEventListener('DOMContentLoaded', () => {
    const ingredientList = document.getElementById('ingredientList');
    const btnAdd = document.getElementById('btnAdd');
    const resVolume = document.getElementById('resVolume');
    const resAbv = document.getElementById('resAbv');
    const resMass = document.getElementById('resMass');

    // 초기 예시 데이터 셋업
    const initialData = [
        { name: '필스너 우르켈', vol: 330, abv: 4.4 },
        { name: '위스키', vol: 30, abv: 40 }
    ];

    // 재료 입력 행 추가 함수
    function addIngredient(nameValue = '', volValue = '', abvValue = '') {
        const row = document.createElement('div');
        row.className = 'ingredient-row';
        
        row.innerHTML = `
            <div class="input-group" style="flex: 1.5;">
                <label>재료명</label>
                <input type="text" placeholder="예: 진, 토닉워터" class="inp-name" value="${nameValue}">
            </div>
            <div class="input-group">
                <label>용량 (ml)</label>
                <input type="number" min="0" placeholder="0" class="inp-vol" value="${volValue}">
            </div>
            <div class="input-group">
                <label>도수 (%)</label>
                <input type="number" min="0" max="100" step="0.1" placeholder="0" class="inp-abv" value="${abvValue}">
            </div>
            <button class="btn-delete" title="삭제">×</button>
        `;
        
        // 생성된 요소에 이벤트 리스너 등록
        row.querySelectorAll('input').forEach(input => {
            input.addEventListener('input', calculate);
        });
        
        row.querySelector('.btn-delete').addEventListener('click', () => {
            row.remove();
            calculate();
        });

        ingredientList.appendChild(row);
        calculate();
    }

    // 도수 및 알코올 계산 로직
    function calculate() {
        const rows = document.querySelectorAll('.ingredient-row');
        
        let numerator = 0;
        let denominator = 0;

        rows.forEach(row => {
            const vol = parseFloat(row.querySelector('.inp-vol').value) || 0;
            const abv = parseFloat(row.querySelector('.inp-abv').value) || 0;
            
            numerator += (vol * abv);
            denominator += vol;
        });

        let finalAbv = 0;
        let alcoholMass = 0;

        if (denominator > 0) {
            finalAbv = (numerator / denominator).toFixed(1);
            alcoholMass = (finalAbv * 0.01 * denominator * 0.785).toFixed(1);
        }

        // 화면 업데이트
        resVolume.textContent = denominator;
        resAbv.textContent = finalAbv;
        resMass.textContent = alcoholMass;
    }

    // 이벤트 바인딩 및 초기화
    btnAdd.addEventListener('click', () => addIngredient('', '', ''));
    
    initialData.forEach(item => addIngredient(item.name, item.vol, item.abv));
    calculate();
});
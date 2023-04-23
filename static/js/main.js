function insertrow(i,a,b,c='notprovided',func_c='notprovided')
{
    if (c === 'notprovided' && func_c == 'notprovided'){
        let row = document.createElement('tr');
        let cell1 = document.createElement('td');
        cell1.innerHTML = i;
        let cell2 = document.createElement('td');
        cell2.innerHTML = a;
        let cell3 = document.createElement('td');
        cell3.innerHTML = b;
        // let cell4 = document.createElement('td');
        // cell4.innerHTML = c;
        // let cell5 = document.createElement('td');
        // cell5.innerHTML = func_c;
        row.appendChild(cell1);
        row.appendChild(cell2);
        row.appendChild(cell3);
        // row.appendChild(cell4);
        // row.appendChild(cell5);
        tbody.appendChild(row);
        row.setAttribute('class','row-class')        
    }
    else{
        let row = document.createElement('tr');
        let cell1 = document.createElement('td');
        cell1.innerHTML = i;
        let cell2 = document.createElement('td');
        cell2.innerHTML = a;
        let cell3 = document.createElement('td');
        cell3.innerHTML = b;
        let cell4 = document.createElement('td');
        cell4.innerHTML = c;
        let cell5 = document.createElement('td');
        cell5.innerHTML = func_c;
        row.appendChild(cell1);
        row.appendChild(cell2);
        row.appendChild(cell3);
        row.appendChild(cell4);
        row.appendChild(cell5);
        tbody.appendChild(row);
        row.setAttribute('class','row-class')
    }
}
function calcbissectroot()
{
    let m = document.getElementById('mistake')
    let expression = document.getElementById('expression').value;
    let first_interval = document.getElementById('1stinterval').value;
    let second_interval = document.getElementById('2ndinterval').value;
    let tolerance_value = document.getElementById('tolerance').value;
    fetch('/bissectionmethod',{
        method: 'POST',
        body: JSON.stringify({
            expression: expression,
            first_interval: first_interval,
            second_interval: second_interval,
            tolerance_value: tolerance_value
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(response => {
        return response.json()
    })
    .then(data => {
        let org_e = expression 
        table = document.getElementById('table')
        if(table.style.display !== 'none')
        {
            tbody = document.getElementById('table-body')
            let arr = Array.from(tbody.rows)
            for(let i=0;i<arr.length;i++)
            {
                document.getElementsByClassName('row-class')[0].remove()
            }
        }
        if(data['message'] != 'ok'){
            table.style.display = 'none'
            m.style.display = 'block'
            ans = document.getElementById('answer')
            ans.innerText = ''
            m.innerText = data['error']    
        }
        else{
            m.style.display = 'none'
            table.style.display = 'table'
            table = data['table']
            iterations = data['iterations']
            ans = data['ans']
            let i = 1
            for(let row of table){
                insertrow(i,row[0],row[1],row[2],row[3])
                i += 1
            }
            ans = document.getElementById('answer')
            ans.innerText = `The root of ${org_e} is ${data['ans']} after ${i-1} iterations`
        }

    })   
}


function calcregulafalsiroot(){
    let m = document.getElementById('mistake')
    let expression = document.getElementById('expression').value;
    let first_interval = document.getElementById('1stinterval').value;
    let second_interval = document.getElementById('2ndinterval').value;
    let tolerance_value = document.getElementById('tolerance').value;
    if (expression === "" || first_interval === "" || second_interval === ""){
        table.style.display = 'none'
        m.style.display = 'block'
        ans = document.getElementById('answer')
        ans.innerText = ''
        m.innerText = "Fields cannot be left empty"
    }
    fetch('/regulafalsimethod',{
        method: 'POST',
        body: JSON.stringify({
            expression: expression,
            first_interval: first_interval,
            second_interval: second_interval,
            tolerance_value: tolerance_value
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(response => {
        return response.json()
    })
    .then(data => {
        let org_e = expression 
        table = document.getElementById('table')
        if(table.style.display !== 'none')
        {
            tbody = document.getElementById('table-body')
            let arr = Array.from(tbody.rows)
            for(let i=0;i<arr.length;i++)
            {
                document.getElementsByClassName('row-class')[0].remove()
            }
        }
        if(data['message'] != 'ok'){
            table.style.display = 'none'
            m.style.display = 'block'
            ans = document.getElementById('answer')
            ans.innerText = ''
            m.innerText = data['error']    
        }
        else{
            m.style.display = 'none'
            table.style.display = 'table'
            table = data['table']
            iterations = data['iterations']
            ans = data['ans']
            let i = 1
            for(let row of table){
                insertrow(i,row[0],row[1],row[2],row[3])
                i += 1
            }
            ans = document.getElementById('answer')
            ans.innerText = `The root of ${org_e} is ${data['ans']} after ${i-1} iterations`
        }

    })
}


function calcnewtonroot(){
    let m = document.getElementById('mistake')
    let expression = document.getElementById('expression').value;
    let first_interval = document.getElementById('1stinterval').value;
    let second_interval = document.getElementById('2ndinterval').value;
    let tolerance_value = document.getElementById('tolerance').value;
    if (expression === "" || first_interval === "" || second_interval === ""){
        table.style.display = 'none'
        m.style.display = 'block'
        ans = document.getElementById('answer')
        ans.innerText = ''
        m.innerText = "Fields cannot be left empty"
    }
    fetch('/newtonmethod',{
        method: 'POST',
        body: JSON.stringify({
            expression: expression,
            first_interval: first_interval,
            second_interval: second_interval,
            tolerance_value: tolerance_value
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(response => {
        return response.json()
    })
    .then(data => {
        let org_e = expression 
        table = document.getElementById('table')
        if(table.style.display !== 'none')
        {
            tbody = document.getElementById('table-body')
            let arr = Array.from(tbody.rows)
            for(let i=0;i<arr.length;i++)
            {
                document.getElementsByClassName('row-class')[0].remove()
            }
        }
        if(data['message'] != 'ok'){
            table.style.display = 'none'
            m.style.display = 'block'
            ans = document.getElementById('answer')
            ans.innerText = ''
            m.innerText = data['error']    
        }
        else{
            m.style.display = 'none'
            table.style.display = 'table'
            table = data['table']
            iterations = data['iterations']
            ans = data['ans']
            let i = 1
            for(let row of table){
                insertrow(i,row[0],row[1])
                i += 1
            }
            ans = document.getElementById('answer')
            ans.innerText = `The root of ${org_e} is ${data['ans']} after ${data['iterations']} iterations at point ${data['point']}`
        }

    })    
}


function calcsecantroot(){
    let m = document.getElementById('mistake')
    let expression = document.getElementById('expression').value;
    let first_interval = document.getElementById('1stinterval').value;
    let second_interval = document.getElementById('2ndinterval').value;
    let tolerance_value = document.getElementById('tolerance').value;
    if (expression === "" || first_interval === "" || second_interval === ""){
        table.style.display = 'none'
        m.style.display = 'block'
        ans = document.getElementById('answer')
        ans.innerText = ''
        m.innerText = "Fields cannot be left empty"
    }
    fetch('/secantmethod',{
        method: 'POST',
        body: JSON.stringify({
            expression: expression,
            first_interval: first_interval,
            second_interval: second_interval,
            tolerance_value: tolerance_value
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(response => {
        return response.json()
    })
    .then(data => {
        let org_e = expression 
        table = document.getElementById('table')
        if(table.style.display !== 'none')
        {
            tbody = document.getElementById('table-body')
            let arr = Array.from(tbody.rows)
            for(let i=0;i<arr.length;i++)
            {
                document.getElementsByClassName('row-class')[0].remove()
            }
        }
        if(data['message'] != 'ok'){
            table.style.display = 'none'
            m.style.display = 'block'
            ans = document.getElementById('answer')
            ans.innerText = ''
            m.innerText = data['error']    
        }
        else{
            m.style.display = 'none'
            table.style.display = 'table'
            table = data['table']
            iterations = data['iterations']
            ans = data['ans']
            let i = 1
            for(let row of table){
                insertrow(i,row[0],row[1],row[2],row[3])
                i += 1
            }
            ans = document.getElementById('answer')
            ans.innerText = `The root of ${org_e} is ${data['ans']} after ${data['iterations']} iterations`
        }

    })
}
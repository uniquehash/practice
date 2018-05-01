chase = (cutoff) => {
	let account = document.getElementById('accountName').children[0].innerText	
	let debit = account === 'CHASE COLLEGE' ? 1 : 0
	let credit = account === 'CREDIT CARD' ? 1 : 0
	let delim = ' | '
	let cdate = new Date(cutoff)
	if (debit)
		debitScrape()
	if (credit)
		creditScrape()
	function debitScrape() {
		let table = document.getElementById('activityTable')
		let rows = [].slice.call(table.children)
		let date = ''
		rows.map(row => {
			let columns = row.children
			date = columns[0].innerText === '' ? date : columns[0].innerText
			let tdate = new Date(date)
			if (cdate <= tdate) {
				let description = columns[1].children[0].innerHTML
				let amount = columns[3].innerText
				if (amount[0] === '−') {
					amount = amount.slice(2)
				} else {
					amount = 'delete'
				}
				console.log(description, delim, amount, delim, date)
			}						
		})	
	}
	function creditScrape(){
		let table = document.getElementById('transactionsBodyId')
		let rows = [].slice.call(table.children)
		let date = ''		
		rows.map(row => {
			if (row.id === 'endOfStatementCycleAccountActivityId')
				return
			let columns = row.children
			date = columns[0].innerText === '' ? date : columns[0].innerText
			let tdate = new Date(date)
			if (cdate <= tdate) {
				let description = columns[1].children[1].innerHTML
				let amount = columns[3].innerText
				if (amount[0] === '−') {
					amount = 'delete'
				} else {
					amount = amount.slice(1)
				}
				console.log(description, delim, amount, delim, date)
			}
		})	
	}
}
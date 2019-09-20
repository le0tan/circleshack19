function initSearchBar() {
	var searchBar = document.getElementById('search');
	var searchTypeAlt = document.getElementById('search-type-alt');
	searchTypeAlt.onclick = toggleSearchType;
	var searchBtn = document.getElementById('search');
	searchBtn.onclick = getIncomeFromPostalCode;
}

function toggleSearchType(searchBar) {
	var searchType = document.getElementById('search-type');
	var searchTypeAlt = document.getElementById('search-type-alt');
	var userInput = document.getElementById('user-input');
	if(searchType.classList.contains('postal')){
		searchType.textContent='Address';
		searchTypeAlt.textContent='Postal';
		searchType.classList.remove('postal');
		searchType.classList.add('address');
		userInput.placeholder='Enter address here';
	}else{
		searchType.textContent='Postal';
		searchTypeAlt.textContent='Address';
		searchType.classList.add('postal');
		searchType.classList.remove('address');
		userInput.placeholder='Enter postal code here';
	}
}

function getIncomeFromPostalCode() {
	var input = document.getElementById('user-input');
	fetch("/api/v1/postal_code_to_income?postal_code="+input.value)
	.then(function(response){
		return response.json();
	})
	.then(function(result) {
		console.log(result);	
	});
}
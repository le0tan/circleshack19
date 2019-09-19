function initSearchBar() {
	var searchBar = document.getElementById('search');
	var searchTypeAlt = document.getElementById('search-type-alt');
	searchTypeAlt.onclick = toggleSearchType;
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
const axios = require('axios');
const cheerio = require('cheerio');

const url = 'https://www.footballoutsiders.com/stats/ncaaoff';

var html = axios.get(url)
    .then(response => {
	return response.data;
    });

function getData(html) {
    data = [];
    const $ = cheerio.load(html);
    $('table.stats tbody tr').each((i, elem) => {
	console.log($(elem).text())
	data.push($(elem).text());
    });

    console.log(data);
}

console.log("Getting data from html...");
getData(html);

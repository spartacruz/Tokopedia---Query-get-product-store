# Tokopedia---Query-get-product-store
A script that helps you to retrive all product_sku on seller store (Tokopedia).

Just download the repo and make some modify on .py. Change the ``parent_dir`` directory based on your environtment.

Each store in Tokopedia have a unique ``shop_id``. 
You only need to provide ``shop_id`` on .txt file, that can be retrive from another tokopedia API.

Here some snippets from their API

``{
	"links": {
		"prev": "",
		"next": "https://ace.tokopedia.com/v1/web-service/shop/get_shop_product?etalase_id=etalase&order_by=1&page=2&per_page=80&shop_id=652660&user_cityId=176&user_districtId=2274",
		"__typename": "ShopProductListLink"
	}
}``

For now, ``shop_id`` have to be provided manually... 

Next project, will add a built-in function to retrive it programmaticaly. User only need to provide a store page link (e.g https://www.tokopedia.com/onemed)


NB:
*This code could be used as long as there is no significant change on tokopedia API
*Do with your own risk.
*I suggest for testing purpose only.

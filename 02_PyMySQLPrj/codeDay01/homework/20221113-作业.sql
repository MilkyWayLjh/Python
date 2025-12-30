-- A. 查询卖的最贵的商品的名称
SELECT goods_name FROM ecs_goods ORDER BY shop_price DESC LIMIT 1;

-- B. 查询商品品牌为"仓品"的 所有商品名称和商品价格
SELECT goods_name, shop_price FROM ecs_goods INNER JOIN ecs_brand USING (brand_id)
WHERE brand_name = '仓品';

-- C. 查询商品品牌为"仓品"的 所有商品名称和商品价格 按照价格降序排列
SELECT goods_name, shop_price FROM ecs_goods INNER JOIN ecs_brand USING (brand_id)
WHERE brand_name = '仓品'
ORDER BY shop_price DESC;

-- D. 查询每个商品品牌的商品数量
SELECT brand_name, COUNT(*) FROM ecs_goods INNER JOIN ecs_brand USING (brand_id)
GROUP BY brand_name;

-- E. 查询商品品牌对应的商品数量大于5的商品品牌名称
SELECT brand_name, COUNT(*) FROM ecs_goods INNER JOIN ecs_brand USING (brand_id)
GROUP BY brand_name HAVING COUNT(*) > 5;


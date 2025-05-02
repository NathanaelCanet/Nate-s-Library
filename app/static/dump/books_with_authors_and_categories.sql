create view view_books_with_authors_and_categories 
AS
SELECT 
    b.id AS book_id,
    b.title,
    b.description,
    b.price,
    b.stock,
    b.image_url,
    b.created_at,
    a.name AS author_name,
    c.name AS category_name
FROM 
    books b
JOIN 
    authors a ON b.author_id = a.id
LEFT JOIN 
    categories c ON b.category_id = c.id;
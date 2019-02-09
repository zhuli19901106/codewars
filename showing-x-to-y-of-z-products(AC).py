def pagination_text(page_number, page_size, total_products):
    x = page_size * (page_number - 1) + 1
    y = min(x + page_size - 1, total_products)
    return 'Showing %d to %d of %d Products.' % (x, y, total_products)
    
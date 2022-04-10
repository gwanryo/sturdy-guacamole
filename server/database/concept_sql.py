concept_operation = {
    "search": '''
        SELECT
            c.concept_id, c.concept_name, c.domain_id
        FROM
            de.concept c
        WHERE
            c.concept_name LIKE %(keyword)s
        ORDER BY
            c.concept_id
        OFFSET
            %(offset)s
        LIMIT
            %(limit)s'''
}
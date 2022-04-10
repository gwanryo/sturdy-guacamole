table_operation = {
    "search": '''
        SELECT
            d.person_id, d.drug_concept_id, c.concept_name, d.drug_exposure_start_date, d.drug_exposure_end_date, d.visit_occurrence_id
        FROM
            de.drug_exposure d
                INNER JOIN de.concept c on d.drug_concept_id = c.concept_id
        WHERE
            c.concept_name LIKE %(keyword)s
        ORDER BY
            d.person_id
        OFFSET
            %(offset)s
        LIMIT
            %(limit)s;
    '''
}
stats_operation = {
    'total': 'SELECT \'total\', COUNT(*) count FROM de.person', 
    'gender': '''
        SELECT
            (
                SELECT
                    c.concept_name
                FROM
                    de.concept c
                WHERE
                    p.gender_concept_id = c.concept_id
            ) concept_name,
            COUNT(*) count
        FROM
            de.person p
        GROUP BY
            p.gender_concept_id''',
    'race': '''
        SELECT
            (
                SELECT
                    c.concept_name
                FROM
                    de.concept c
                WHERE
                    p.race_concept_id = c.concept_id
            ) concept_name,
            COUNT(*) count
        FROM
            de.person p
        GROUP BY
            p.race_concept_id''',
    'ethnicity': '''
        SELECT
            (
                SELECT
                    c.concept_name
                FROM
                    de.concept c
                WHERE
                    p.ethnicity_concept_id = c.concept_id
            ) concept_name,
            COUNT(*) count
        FROM
            de.person p
        GROUP BY
            p.ethnicity_concept_id''',
    'death': 'SELECT  \'death\', COUNT(*) count FROM de.death'
}


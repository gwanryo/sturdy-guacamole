stats_operation = {
    'total': '''
        SELECT
            (
                SELECT
                    c.concept_name
                FROM
                    de.concept c
                WHERE
                    o.visit_concept_id = c.concept_id
            ) concept_name,
            COUNT(*) count
        FROM
            de.visit_occurrence o
        GROUP BY
            o.visit_concept_id''',
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
            de.visit_occurrence o
                INNER JOIN de.person p on o.person_id = p.person_id
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
            de.visit_occurrence o
                INNER JOIN de.person p on o.person_id = p.person_id
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
            de.visit_occurrence o
                INNER JOIN de.person p on o.person_id = p.person_id
        GROUP BY
            p.ethnicity_concept_id''',
    'age_group': '''
        SELECT
            CAST((FLOOR(DATE_PART('year', AGE(p.birth_datetime)) / 10) * 10) AS INT) age_group,
            COUNT(*)
        FROM
            de.visit_occurrence o
                INNER JOIN de.person p on o.person_id = p.person_id
        GROUP BY
            age_group
        ORDER BY
            age_group'''
}
"""
Basic set statistics
"""
from es_core.es_search import BaseSearch
from es_core.utils import (
    execute_aggs,
    check_term_field
)
from es_core.utils import create_range_buckets


@execute_aggs
@check_term_field
def term_aggs_by_field(field):
    qs = BaseSearch().agg_search()
    qs.aggs.bucket(
        name='agg', agg_type='terms', field=field, size=50,
        order={'_key': 'asc'}
    )
    return qs


@execute_aggs
def salary_by_age():
    qs = BaseSearch().agg_search()
    qs.aggs.bucket(
        name='agg', agg_type='terms', field='Age', size=50,
        order={'_key': 'asc'}
    ).metric('avg_salary', 'avg', field='Salary')
    return qs


@execute_aggs
def salary_by_bucket_ages():
    qs = BaseSearch().agg_search()
    qs.aggs.bucket(
        name='salary_by_buckets_dist', agg_type='range',
        field='Age', ranges=create_range_buckets(20, 55, 5)
    ).metric('avg_salary', 'avg', field='Salary')
    return qs


@execute_aggs
def salary_by_gender():
    qs = BaseSearch().agg_search()
    qs.aggs.bucket(
        name='salary_by_gender', agg_type='terms', field='Gender'
    ).metric('avg_salary', 'avg', field='Salary')
    return qs


@execute_aggs
def salary_by_gender_age_buckets():
    qs = BaseSearch().agg_search()
    qs.aggs.bucket(
        name='salary_by_buckets_dist', agg_type='range',
        field='Age', ranges=create_range_buckets(20, 55, 5)
    ).bucket('get_gender', 'terms', field='Gender'
    ).metric('avg_salary', 'avg', field='Salary')
    return qs
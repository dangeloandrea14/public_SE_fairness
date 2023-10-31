from icecream import ic
from aif360.datasets import BinaryLabelDataset
from aif360.metrics import BinaryLabelDatasetMetric


def _get_groups(data, label_name, positive_label, group_condition):
    query = "&".join([str(k) + "==" + str(v) for k, v in group_condition.items()])
    label_query = label_name + "==" + str(positive_label)
    unpriv_group = data.query(query)
    unpriv_group_pos = data.query(query + "&" + label_query)
    priv_group = data.query("~(" + query + ")")
    priv_group_pos = data.query("~(" + query + ")&" + label_query)
    return unpriv_group, unpriv_group_pos, priv_group, priv_group_pos


def _compute_probs(data_pred, label_name, positive_label, group_condition):
    unpriv_group, unpriv_group_pos, priv_group, priv_group_pos = _get_groups(
        data_pred, label_name, positive_label, group_condition
    )
    unpriv_group_prob = len(unpriv_group_pos) / len(unpriv_group)
    priv_group_prob = len(priv_group_pos) / len(priv_group)
    return unpriv_group_prob, priv_group_prob


def disparate_impact(data_pred, group_condition, label_name, positive_label):
    unpriv_group_prob, priv_group_prob = _compute_probs(
        data_pred, label_name, positive_label, group_condition
    )
    return (
        min(unpriv_group_prob / priv_group_prob, priv_group_prob / unpriv_group_prob)
        if unpriv_group_prob != 0 and priv_group_prob != 0
        else 0
    )
    # return di_aif360(data_pred, label_name, group_condition, positive_label)


def di_aif360(df, label_name, group_condition, favorable_label):
    dataset = BinaryLabelDataset(
        df=df,
        label_names=[label_name],
        protected_attribute_names=group_condition.keys(),
        favorable_label=favorable_label,
    )
    metrics = BinaryLabelDatasetMetric(
        dataset, privileged_groups=[{"Genere": 1}], unprivileged_groups=[{"Genere": 0}]
    )
    return metrics.disparate_impact()

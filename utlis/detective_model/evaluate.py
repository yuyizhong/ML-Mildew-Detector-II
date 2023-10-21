import streamlit as st
import joblib


def load_model_evaluation(version):
    return joblib.load(f'outputs/{version}/evaluation.pkl')
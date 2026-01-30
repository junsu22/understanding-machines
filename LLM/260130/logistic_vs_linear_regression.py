import plotly.graph_objects as go
import numpy as np

# 데이터 생성
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
pass_fail = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

# 부드러운 곡선
x_smooth = np.linspace(0, 11, 200)

# 선형 회귀
w = 0.18
b = -0.9
y_linear = w * x_smooth + b

# 로지스틱 회귀
w_logistic = 2
b_logistic = -10
z = w_logistic * x_smooth + b_logistic
y_logistic = 1 / (1 + np.exp(-z))


# 그래프 그리기
fig = go.Figure()

# 실제 데이터 (산점도)
fig.add_trace(
    go.Scatter(
        x=study_hours,
        y=pass_fail,
        mode="markers",
        name="실제데이터",
        marker=dict(size=10, color="black"),
    )
)


# 선형회귀선
fig.add_trace(
    go.Scatter(
        x=x_smooth,
        y=y_linear,
        mode="lines",
        name="선형 회귀",
        line=dict(color="red", dash="dash", width=2),
    )
)

# 로지스틱 회귀선
fig.add_trace(
    go.Scatter(
        x=x_smooth,
        y=y_logistic,
        mode="lines",
        name="로지스틱 회귀 (시그모이드)",
        line=dict(color="blue", width=3),
    )
)

# 분류 기준선(0.5)
fig.add_hline(
    y=0.5, line_dash="dot", line_color="green", annotation_text="분류 기준 : 0.5"
)

# 레이아웃 설정
fig.update_layout(
    title="선형회귀 VS 로지스틱 회귀 비교하기",
    xaxis_title="공부시간(hours)",
    yaxis_title="합격확률",
    yaxis=dict(range=[-0.5, 1.5]),  # y축의 범위
    showlegend=True,
    width=900,
    height=600,
)
fig.show()

# Quantumult X 中国大陆分流规则

基于 [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) 整理。

## 直接使用地址

完整配置片段：

```text
https://raw.githubusercontent.com/fox37x/qx-rules/main/QuantumultX/qx-china.conf
```

只要远程规则：

```text
https://raw.githubusercontent.com/fox37x/qx-rules/main/QuantumultX/filter_remote.conf
```

## 设计

- 广告：`reject`
- 国内 / 局域网 / 国内媒体：`direct`
- AI / Telegram / Google / YouTube / GitHub / 海外媒体：`PROXY` 分组
- Apple / Microsoft：默认 `direct`，可手动切到代理
- `FINAL,PROXY` 兜底

## 自动同步

GitHub Actions 每天同步一次上游规则文件到 `rules/QuantumultX/*/*.list`。
也可以在 Actions 页面手动运行 `Sync upstream rules`。

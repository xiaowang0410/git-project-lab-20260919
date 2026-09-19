# 项目协作约定

## 成员与职责

本次为单人实验，仓库所有者 xiaowang0410 负责维护仓库、实现功能、验证结果和维护工单，拥有 Admin 权限。工单通过 Assignees 明确责任人。多人项目可由所有者在 Settings → Collaborators 邀请成员，再按职责分配权限。

## 分支与合并

main 保存可运行版本；feature/task-summary 用于功能开发；docs/collaboration 用于文档改进。先提交并推送分支，再创建 Pull Request 检查 Files changed，确认后合并到 main。

## 任务状态

工单使用 status:todo、status:in-progress、status:done 记录待办、进行中和已完成。完成验收后关闭工单，并保留提交或 Pull Request 链接。实验一 v1.0 里程碑用于汇总本次验收范围。

## 验收结果

任务统计程序对空任务列表返回 total=0、done=0、pending=0；对一项完成、一项待办的数据返回 total=2、done=1、pending=1。

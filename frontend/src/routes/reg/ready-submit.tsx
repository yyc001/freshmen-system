import { createFileRoute } from '@tanstack/react-router'
import PageContent from '../../components/PageContent'
import { Button, Space } from 'antd'
import axios from 'axios';
export const Route = createFileRoute('/reg/ready-submit')({
  loader: async (params : any) => {
    params = params.location.search;
    console.log(params)
    let uid = params.uid;
    if (!uid) {
      const response = await axios.get('/api/whoami');
      uid = response.data.uid;
    }
    const material = await axios.get('/api/student/check/info', {params: {uid: uid}});
    const manual_check = await axios.get('/api/student/check/get', {params: {uid: uid}});
    console.log(manual_check.data)
    return Object.assign({uid: uid}, material.data, manual_check.data)
  },
  component: () => {
    const loader_data = Route.useLoaderData();
    console.log(loader_data)
    const submission = () => {
      axios.post('/api/student/check/change', {uid: loader_data.uid, to: 1})
      .then(() => {
        window.location.reload()
      })
    }
    const revoke = () => {
      axios.post('/api/student/check/change', {uid: loader_data.uid, to: 4})
      .then(() => {
        window.location.reload()
      })
    }
    return (
      <>
    <PageContent>
        <h1> 报名 · 第五步 </h1>
        <div
            style={{
                minHeight: 280,
                // borderRadius: borderRadiusLG,
                maxWidth: 1000,
                margin: "auto"
            }}
        >
            <h2> 材料完整性 </h2>
            <p> 联系方式: {loader_data.tel}</p>
            <p> 基本信息: {loader_data.info}</p>
            <p> 附件: {loader_data.attachments}</p>
            <h2> 材料核验情况 </h2>
            <p> 剩余次数: {loader_data.remain}</p>
            <p> 状态: {loader_data.status_name}</p>
            <p> 审核意见: {loader_data.comment}</p>
            <Space>
                <Button href='/reg/attachments'>上一步</Button>
                <Button type='primary' onClick={submission} disabled={!(loader_data.complete && loader_data.allow_submit)}>提交申请</Button>
                <Button onClick={revoke} disabled={!loader_data.allow_revoke}>撤销申请</Button>
            </Space>
        </div>

      </PageContent>
      </>
    )
  },
})
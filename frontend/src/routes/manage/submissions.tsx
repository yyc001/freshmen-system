import { createFileRoute } from '@tanstack/react-router'
import PageContent from '../../components/PageContent'
import { Table } from 'antd'
import Link from 'antd/es/typography/Link'
import axios from 'axios'

const dataSourceLink = (data: any) => {
  const newData = data.map((item: any) => ({
    ...item,
    key: item.uid,
    option: <Link href={`/manage/view/${item.uid}`}> 查看详情 </Link>,
  }));
  return newData
}

export const Route = createFileRoute('/manage/submissions')({
  loader: async () => {
    const response = await axios.get('/api/student/list');
    return response.data
  },
  component: () => {
    const loader_data = Route.useLoaderData();
    console.log(loader_data)
    return (
      <>
        <PageContent>
          <h1> 学生管理 </h1>
          <Table 
            dataSource={dataSourceLink(loader_data.students)} 
            columns={[
                {
                    title: '学号',
                    dataIndex: 'uid',
                    key: 'uid',
                },
                {
                    title: '姓名',
                    dataIndex: 'name',
                    key: 'name',
                },
                {
                    title: '状态',
                    dataIndex: 'status_name',
                    key: 'status_name',
                },
                {
                    title: '操作',
                    dataIndex: 'option',
                    key: 'option',
                },
            ]} 
          />
        </PageContent> 
      </>
    )
  },
})